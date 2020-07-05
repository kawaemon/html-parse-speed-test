NODE_COUNT = 400
COLOR_GROUP_COUNT = 400
COLORS = ["red", "green", "blue"]

# nest + a little css test.

"""
<ul>
  <li style="color: COLORS[index]"> index </li>
  ... NODE_COUNT
  <ul>
      <li style="..."> index </li>
      ...NODE_COUNT
      <ul> ...COLOR_GROUP_COUNT </ul>
  </ul>
</ul>
"""


def gen(count):
    color_index = 0

    print("<ul>")

    for x in range(NODE_COUNT):
        print(
            "    <li style=\"color:{}\">{}</li>".format(COLORS[color_index], x))
        color_index += 1
        if color_index == len(COLORS):
            color_index = 0

    if count != 0:
        gen(count - 1)

    print("</ul>")


print("<!doctype html>")
print("<html>")
print("<body>")
print("<div class=\"render_time\"></div>")
print("<script type=\"text/javascript\" src=\"check-render-time.js\"></script>")

gen(COLOR_GROUP_COUNT)

print("</body>")
print("</html>")
