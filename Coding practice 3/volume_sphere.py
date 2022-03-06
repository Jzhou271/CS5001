"""
Coding practice -- Module 3
5. Volume of a sphere
Write a function called volume_sphere that receives the radius of a sphere,
and returns the volume of the sphere.
For your implementation, assume PI = 3.14159
"""


def volume_sphere(radius):
    PI = 3.14159
    return (4 / 3) * PI * radius ** 3


def main():
    print(volume_sphere(2))
    print(volume_sphere(10))


if __name__ == "__main__":
    main()
