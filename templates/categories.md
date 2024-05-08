---
hide:
  - navigation
---

# Categories

{% for subsection in projects %}

## {{ subsection.title}}

{% for project in subsection.projects %}

??? example "[{{ project.name }}]({{ project.url }})<br>{{ project.description }}"
    <a href="{{ project.url }}">
    <img src="{{ project.images }}" align="center">
    </a>
{% endfor %}
{% endfor %}
