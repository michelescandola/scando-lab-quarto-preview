```{=html}
<div class="publication-toolbar" role="group" aria-label="Filter publications">
  <button class="filter-button" type="button" data-filter="all" aria-pressed="true">All selected work</button>
  <button class="filter-button" type="button" data-filter="statistics" aria-pressed="false">Statistics &amp; methods</button>
  <button class="filter-button" type="button" data-filter="body" aria-pressed="false">Body, pain &amp; cognition</button>
</div>
<p class="filter-status" role="status" aria-live="polite" aria-atomic="true"></p>
<div class="publication-list">
<% for (const item of items) { %>
  <article class="publication" data-category="<%- item.category %>">
    <div class="publication-meta"><%- item.label %><br><%- item.year %></div>
    <div class="publication-copy">
      <h2><%- item.title %></h2>
      <p><%- item.authors %></p>
    </div>
    <a class="publication-link" href="<%- item.url %>" target="_blank" rel="noopener noreferrer"
       aria-label="Read <%- item.title %>">↗</a>
  </article>
<% } %>
</div>
```
