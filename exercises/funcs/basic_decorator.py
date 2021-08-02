def decorator(func):
    def environment() -> None:
        print("Decoring environment...")
        func()
        print("Done!")

    return environment


def saludo():
    print("Hi!")


saludo()
# Output: Hi!

print("------------")

saludo_decorated = decorator(saludo)
saludo_decorated()
