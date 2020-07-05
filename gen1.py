NODE_COUNT = 60000

# no nest test

print("<!doctype html>")
print("<html>")
print("<body>")
print("<div class=\"render_time\"></div>")
print("<script type=\"text/javascript\" src=\"check-render-time.js\"></script>")

for x in range(NODE_COUNT):
    print("<div>{}</div>".format(x))

print("</body>")
print("</html>")
