```{=html}
<%
// ISO dates sort chronologically as text. Partial dates keep their known
// precision: a year-only record follows dated records from that same year.
const publications = items.slice().sort((a, b) =>
  String(b.published).localeCompare(String(a.published)) || a.title.localeCompare(b.title)
);
const topics = templateParams.topics;
function dateLabel(value) {
  const parts = String(value).split("-").map(Number);
  if (parts.length === 1) return String(parts[0]);
  const options = { month: "short", year: "numeric", timeZone: "UTC" };
  if (parts.length === 3) options.day = "numeric";
  return new Intl.DateTimeFormat("en-GB", options).format(
    new Date(Date.UTC(parts[0], parts[1] - 1, parts[2] || 1))
  );
}
%>
<div class="publication-toolbar" role="group" aria-label="Filter publications">
  <button class="filter-button" type="button" data-filter="all" aria-pressed="true">All publications</button>
<% for (const topic of topics) { %>
  <button class="filter-button" type="button" data-filter="<%- topic.id %>" aria-pressed="false"><%- topic.text %></button>
<% } %>
</div>
<p class="filter-status" role="status" aria-live="polite" aria-atomic="true"><%- publications.length %> publications · All topics · Newest first</p>
<noscript><p>All publications are shown below. Enable JavaScript to filter by topic.</p></noscript>
<div class="publication-list">
<% for (const item of publications) { %>
  <article class="publication" data-topics="<%- item.topics.join(' ') %>" data-published="<%- item.published %>">
    <div class="publication-meta">
      <span class="publication-date"><%- dateLabel(item.published) %></span>
      <span class="publication-type"><%- item.publication_type %></span>
    </div>
    <div class="publication-copy">
      <h2><%- item.title %></h2>
      <p class="publication-authors"><%- item.authors %></p>
      <p class="publication-venue"><%- item.venue %></p>
      <% if (item.note) { %><p class="publication-note"><%- item.note %></p><% } %>
      <ul class="publication-topics" aria-label="Research topics">
      <% for (const topic of topics.filter((topic) => item.topics.includes(topic.id))) { %>
        <li><%- topic.text %></li>
      <% } %>
      </ul>
      <a class="publication-source" href="<%- item.source_url %>" target="_blank" rel="noopener noreferrer"
         aria-label="Bibliographic record for <%- item.title %>">Bibliographic record ↗</a>
    </div>
    <a class="publication-link" href="<%- item.url %>" target="_blank" rel="noopener noreferrer"
       aria-label="Read <%- item.title %>">↗</a>
  </article>
<% } %>
</div>
```
