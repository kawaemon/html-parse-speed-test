NODE_COUNT = 60000

# nest test.

print("<!doctype html>")
print("<html>")
print("<body>")
print("<div class=\"render_time\"></div>")
print("<script type=\"text/javascript\" src=\"check-render-time.js\"></script>")

for x in range(NODE_COUNT):
    print("<div>")

print("hello")

for x in range(NODE_COUNT):
    print("</div>")

print("</body>")
print("</html>")
