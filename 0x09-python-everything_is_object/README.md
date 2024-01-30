0x09. Python - Everything is object

9.10. Objects and values
If we execute these assignment statements,

a = "banana"
b = "banana"
we know that a and b will refer to a string with the letters "banana". But we don’t know yet whether they point to the same string.

There are two possible states:

Two state diagrams for multiple references with strings
In one case, a and b refer to two different things that have the same value. In the second case, they refer to the same thing. These things have names — they are called objects.

Mutable and immutable objects
Common immutable type:

numbers: int(), float(), complex()
immutable sequences: str(), tuple(), frozenset(), bytes()
Common mutable type (almost everything else):

mutable sequences: list(), bytearray()
set type: set()
mapping type: dict()
classes, class instances
