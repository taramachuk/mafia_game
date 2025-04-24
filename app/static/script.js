function sender() {
    fetch("/test", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ name: "Alice" })
    })
}
