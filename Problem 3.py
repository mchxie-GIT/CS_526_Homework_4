from math import gcd

def count_right_triangles(points):
    answer = 0

    #Treat each point as the possible right-angle vertex.
    for i, (px, py) in enumerate(points):
        directions = {}

        for j, (x, y) in enumerate(points):
            if i == j:
                continue

            dx = x - px
            dy = y - py

            #Reduce the direction to an exact integer pair.
            divisor = gcd(dx, dy)
            dx //= divisor
            dy //= divisor

            #Opposite vectors lie on the same line through the vertex.
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy

            #A 90-degree rotation gives a perpendicular direction.
            perpendicular_x = -dy
            perpendicular_y = dx
            if perpendicular_x < 0 or (
                perpendicular_x == 0 and perpendicular_y < 0
            ):
                perpendicular_x = -perpendicular_x
                perpendicular_y = -perpendicular_y

            #Match only earlier points, so each pair is counted once.
            perpendicular = (perpendicular_x, perpendicular_y)
            answer += directions.get(perpendicular, 0)

            direction = (dx, dy)
            directions[direction] = directions.get(direction, 0) + 1

    return answer

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    answer = count_right_triangles(points)
    print(f"The number of right triangles is: {answer}")


if __name__ == "__main__":
    main()
