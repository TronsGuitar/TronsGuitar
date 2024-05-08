---
hide:
  - navigation
  - toc
---

# Tools

{% for project in projects %}
??? example "[{{ project.name }}]({{ project.url }}) <br>{{ project.description }}"
    <a href="{{ project.url }}">
    <img src="{{ project.images }}" align="center">
    </a>
{% endfor %}