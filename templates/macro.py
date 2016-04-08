{% extends "parent.html" %}
  {% block content %}
   <h3 style="color:brown;"> This is the start of my child template</h3>
      <br>
      <p>My string: {{my_string}}</p>
      <p>Value from the list: {{my_list[3]}}</p>
      <p>Loop through parentst:</p>
      <ul>
        {% for n in my_list %}
        <li>{{n}}</li>
        {% endfor %}
      </ul>
      <p>Same list but with a filter: {{ my_list|join(', ') }}</p>
      {% filter upper%}
      <p>this text will be upper</p>
      {%endfilter%}
      <h3> This is the end of my child template</h3>
      {% block page %}Home{% endblock %}
      {% block footer %}
        {{super()}}
      {% endblock %}
    {% endblock %}