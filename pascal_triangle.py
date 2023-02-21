def generate_pascals_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle


if __name__ == '__main__':
    # GENERATE TRIANGLE
    pascals_triangle = generate_pascals_triangle(15)
    for row in pascals_triangle:
        print(row)

    # ASSERT
    assert pascals_triangle[0] == [1]
    assert pascals_triangle[1] == [1, 1]
    assert pascals_triangle[2] == [1, 2, 1]
    assert pascals_triangle[3] == [1, 3, 3, 1]
    assert pascals_triangle[4] == [1, 4, 6, 4, 1]
    assert pascals_triangle[5] == [1, 5, 10, 10, 5, 1]
