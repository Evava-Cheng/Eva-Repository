from functions import volume_calculator, sphere_volume, cube_volume, cuboid_volume, cone_volume, cylinder_volume


def test_sphere_volume():
    """Test the sphere_volume function"""

    assert callable(sphere_volume)

    # Test the volume of the sphere with radius of 3.
    radius = 3
    assert sphere_volume(radius) == 113.09733552923254

    # Test the volume of the sphere with radius of 5.
    radius = 5
    assert sphere_volume(radius) == 523.5987755982989


def test_cube_volume():
    """Test the cube_volume function"""

    assert callable(cube_volume)

    # Test the volume of the cube with length of 3.
    length = 3
    assert cube_volume(length) == 27.0

    # Test the volume of the cube with length of 5.
    length = 5
    assert cube_volume(length) == 125.0


def test_cuboid_volume():
    """Test the cuboid_volume function"""

    assert callable(cuboid_volume)

    # Test the volume of the cuboid with width of 3, height of 4, length of 5.
    width = 3
    height = 4
    length = 5
    assert cuboid_volume(width, height, length) == 60.0

    # Test the volume of the cuboid with width of 1, height of 1, length of 10.
    width = 1
    height = 1
    length = 10
    assert cuboid_volume(width, height, length) == 10.0


def test_cone_volume():
    """Test the cone_volume function"""

    assert callable(cone_volume)

    # Test the volume of the cone with radius of 3, height of 4.
    radius = 3
    height = 4
    assert cone_volume(radius, height) == 37.69911184307752

    # Test the volume of the cone with radius of 5, height of 10.
    radius = 5
    height = 10
    assert cone_volume(radius, height) == 261.79938779914943


def test_cylinder_volume():
    """Test the cylinder_volume function"""

    assert callable(cylinder_volume)

    # Test the volume of the cylinder with radius of 3, height of 4.
    radius = 3
    height = 4
    assert cylinder_volume(radius, height) == 113.09733552923255

    # Test the volume of the cylinder with radius of 5, height of 10.
    radius = 5
    height = 10
    assert cylinder_volume(radius, height) == 785.3981633974483
