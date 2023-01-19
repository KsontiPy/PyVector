class Point2:
	
	def __init__(self, x: float, y: float) -> None:
		
		self.x = float(x)
		self.y = float(y)
		
	def __iadd__(self, other):
		
		x = self.x + other.x
		y = self.y + other.y
		
		return Point2(x, y)
		
	def __isub__(self, other):
		
		x = self.x - other.x
		y = self.y - other.y
		
		return Point2(x, y)
		
	def __imul__(self, other):
		
		x = self.x * other.x
		y = self.y * other.y
		
		return Point2(x, y)
		
	def __imod__(self, other):
		
		x = self.x % other.x
		y = self.y % other.y
		
		return Point2(x, y)
		
	def __itruediv__(self, other):
		
		x = self.x / other.x
		y = self.y / other.y
		
		return Point2(x, y)
		
	def __ifloordiv__(self, other):
		
		x = self.x // other.x
		y = self.y // other.y
		
		return Point2(x, y)
		
	def __ipow__(self, other):
		
		x = self.x ** other.x
		y = self.y ** other.y
		
		return Point2(x, y)
		
	def __iand__(self, other):
		
		x = self.x & other.x
		y = self.y & other.y
		
		return Point2(x, y)
		
	def __ior__(self, other):
		
		x = self.x | other.x
		y = self.y | other.y
		
		return Point2(x, y)
		
	def __ixor__(self, other):
		
		x = self.x ^ other.x
		y = self.y ^ other.y
		
		return Point2(x, y)
		
	def __bool__(self):
		
		return self.x != 0 and self.y != 0
		
	def get(self):
		
		return (self.x, self.y)
		
class Vector2:
	
	def __init__(self, start: Point2, end: Point2) -> None:
		
		self.start = start
		self.end = end
		
	def __iadd__(self, vector):
		
		start = self.start
		start += vector.start
		
		end = self.end
		end += vector.end
		
		return Vector2(start, end)
		
	def __isub__(self, vector):
		
		start = self.start
		start -= vector.start
		
		end = self.end
		end -= vector.end
		
		return Vector2(start, end)
		
	def __imul__(self, vector):
		
		start = self.start
		start *= vector.start
		
		end = self.end
		end *= vector.end
		
		return Vector2(start, end)
		
	def __imod__(self, vector):
		
		start = self.start
		start %= vector.start
		
		end = self.end
		end %= vector.end
		
		return Vector2(start, end)
		
	def __itruediv__(self, vector):
		
		start = self.start
		start /= vector.start
		
		end = self.end
		end /= vector.end
		
		return Vector2(start, end)
		
	def __ifloordiv__(self, vector):
		
		start = self.start
		start //= vector.start
		
		end = self.end
		end //= vector.end
		
		return Vector2(start, end)
		
	def __ipow__(self, vector):
		
		start = self.start
		start **= vector.start
		
		end = self.end
		end **= vector.end
		
		return Vector2(start, end)
		
	def __iand__(self, vector):
		
		start = self.start
		start &= vector.start
		
		end = self.end
		end &= vector.end
		
		return Vector2(start, end)
		
	def __ior__(self, vector):
		
		start = self.start
		start |= vector.start
		
		end = self.end
		end |= vector.end
		
		return Vector2(start, end)
		
	def __ixor__(self, vector):
		
		start = self.start
		start ^= vector.start
		
		end = self.end
		end ^= vector.end
		
		return Vector2(start, end)
		
	def __bool__(self):
		
		return self.start.x != self.end.x and self.start.y != self.end.y
		
	def get(self):
		
		return (self.start.x, self.start.y, self.end.x, self.end.y)
		
	def getL(self):
		
		return (self.end.x - self.start.x, self.end.y - self.start.y)
		
class Point3:
	
	def __init__(self, x: float, y: float, z: float) -> None:
		
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
		
	def __iadd__(self, other):
		
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		
		return Point3(x, y, z)
		
	def __isub__(self, other):
		
		x = self.x - other.x
		y = self.y - other.y
		z = self.z - other.z
		
		return Point3(x, y, z)
		
	def __imul__(self, other):
		
		x = self.x * other.x
		y = self.y * other.y
		z = self.z * other.z
		
		return Point3(x, y, z)
		
	def __imod__(self, other):
		
		x = self.x % other.x
		y = self.y % other.y
		z = self.z % other.z
		
		return Point3(x, y, z)
		
	def __itruediv__(self, other):
		
		x = self.x / other.x
		y = self.y / other.y
		z = self.z / other.z
		
		return Point3(x, y, z)
		
	def __ifloordiv__(self, other):
		
		x = self.x // other.x
		y = self.y // other.y
		z = self.z // other.z
		
		return Point3(x, y, z)
		
	def __ipow__(self, other):
		
		x = self.x ** other.x
		y = self.y ** other.y
		z = self.z ** other.z
		
		return Point3(x, y, z)
		
	def __iand__(self, other):
		
		x = self.x & other.x
		y = self.y & other.y
		z = self.z & other.z
		
		return Point3(x, y, z)
		
	def __ior__(self, other):
		
		x = self.x | other.x
		y = self.y | other.y
		z = self.z | other.z
		
		return Point3(x, y, z)
		
	def __ixor__(self, other):
		
		x = self.x ^ other.x
		y = self.y ^ other.y
		z = self.z ^ other.z
		
		return Point3(x, y, z)
		
	def __bool__(self):
		
		return self.x != 0 and self.y != 0 and self.z != 0
		
	def get(self):
		
		return (self.x, self.y, self.z)
		
class Vector3:
	
	def __init__(self, start: Point3, end: Point3) -> None:
		
		self.start = start
		self.end = end
		
	def __iadd__(self, vector):
		
		start = self.start
		start += vector.start
		
		end = self.end
		end += vector.end
		
		return Vector3(start, end)
		
	def __isub__(self, vector):
		
		start = self.start
		start -= vector.start
		
		end = self.end
		end -= vector.end
		
		return Vector3(start, end)
		
	def __imul__(self, vector):
		
		start = self.start
		start *= vector.start
		
		end = self.end
		end *= vector.end
		
		return Vector3(start, end)
		
	def __imod__(self, vector):
		
		start = self.start
		start %= vector.start
		
		end = self.end
		end %= vector.end
		
		return Vector3(start, end)
		
	def __itruediv__(self, vector):
		
		start = self.start
		start /= vector.start
		
		end = self.end
		end /= vector.end
		
		return Vector3(start, end)
		
	def __ifloordiv__(self, vector):
		
		start = self.start
		start //= vector.start
		
		end = self.end
		end //= vector.end
		
		return Vector3(start, end)
		
	def __ipow__(self, vector):
		
		start = self.start
		start **= vector.start
		
		end = self.end
		end **= vector.end
		
		return Vector3(start, end)
		
	def __iand__(self, vector):
		
		start = self.start
		start &= vector.start
		
		end = self.end
		end &= vector.end
		
		return Vector3(start, end)
		
	def __ior__(self, vector):
		
		start = self.start
		start |= vector.start
		
		end = self.end
		end |= vector.end
		
		return Vector3(start, end)
		
	def __ixor__(self, vector):
		
		start = self.start
		start ^= vector.start
		
		end = self.end
		end ^= vector.end
		
		return Vector3(start, end)
		
	def __bool__(self):
		
		return self.start.x != self.end.x and self.start.y != self.end.y
		
	def get(self):
		
		return (self.start.x, self.start.y, self.start.z, self.end.x, self.end.y, self.end.z)
		
	def getL(self):
		
		return (self.end.x - self.start.x, self.end.y - self.start.y, self.end.z - self.start.z)
		
