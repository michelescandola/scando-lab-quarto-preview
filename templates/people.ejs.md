```{=html}
<div class="people-grid">
<% for (const item of items) { %>
  <article class="person">
    <div class="avatar" aria-hidden="true">
      <% if (item.image) { %>
        <img src="<%- item.image %>" alt="" width="75" height="75" loading="lazy" decoding="async">
      <% } else { %><%- item.initials %><% } %>
    </div>
    <h2><%- item.title %></h2>
    <p class="person-role"><%- item.role %></p>
    <p><%- item.description %></p>
    <% if (item.profile_url) { %>
      <a class="profile-link" href="<%- item.profile_url %>" target="_blank" rel="noopener noreferrer">
        University profile <span aria-hidden="true">↗</span>
      </a>
    <% } %>
  </article>
<% } %>
</div>
```
