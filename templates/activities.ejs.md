```{=html}
<% if (items.length === 0) { %>
  <div class="empty-state">
    <h3>More to come.</h3>
    <p>Talks, workshops and other announcements will appear here as they are added.</p>
    <a class="profile-link" href="contact.html">Get in touch <span aria-hidden="true">↗</span></a>
  </div>
<% } else { %>
  <div class="resource-grid">
  <% for (const item of items) { %>
    <article class="resource-card activity-card">
      <p class="card-kicker"><%- item.date_label %></p>
      <h3><%- item.title %></h3>
      <p><%- item.description %></p>
      <% if (item.url) { %>
        <a class="profile-link" href="<%- item.url %>">Details <span aria-hidden="true">↗</span></a>
      <% } %>
    </article>
  <% } %>
  </div>
<% } %>
```
