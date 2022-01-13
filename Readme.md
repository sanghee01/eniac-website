sudo lsof -t -i tcp:8000 | xargs kill -9

<a style="text-decoration: none; color: white;" href="{% url 'user:logout' %}">Log out </a>
