""" ----- *ARGS  -----

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")"""

""" ----- **KWARGS -----
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="123 Fake St.",
              city="Porto Alegre",
              state="RS",
              cep="12345678")"""

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('cep')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               city="Porto Alegre",
               state="RS",
               cep="12345678")
