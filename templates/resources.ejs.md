```{=html}
<div class="resource-grid">
<% for (const item of items) { %>
  <article class="resource-card">
    <p class="card-kicker"><%- item.kind %></p>
    <h2><%- item.title %></h2>
    <p><%- item.description %></p>
    <a class="profile-link" href="<%- item.url %>" target="_blank" rel="noopener noreferrer">
      Open resource <span aria-hidden="true">↗</span>
    </a>
  </article>
<% } %>
</div>
```
