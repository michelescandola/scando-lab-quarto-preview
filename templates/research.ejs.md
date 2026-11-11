```{=html}
<div class="theme-grid">
<% for (const item of items) { %>
  <article class="theme-card <%- item.card_class %>">
    <span class="theme-index"><%- String(item.order).padStart(2, '0') %></span>
    <h2><%- item.title %></h2>
    <p><%- item.description %></p>
  </article>
<% } %>
</div>
```
