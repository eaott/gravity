HEIGHT = 61.5

times = list()
val = " "
while len(val) > 0:
	val = raw_input("time: ")
	if len(val) > 0:
		times.append(float(val))
avg_time = sum(times)/len(times)
avg_g = 2 * HEIGHT / (avg_time ** 2)
std_time = ((1.0/(len(times) - 1) * sum(map(lambda x: (x - avg_time) ** 2, times)))) ** (0.5)
std_g = ((4 * HEIGHT / (avg_time ** 3)) ** 2 * (std_time ** 2)) ** (0.5)
print "RLM Height:",HEIGHT,"m"
print "avg_time:",avg_time,"s"
print "std_time:",std_time,"s"
print "g:",avg_g,"+/-",std_g,"m/s^2"