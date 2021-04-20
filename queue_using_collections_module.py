from collections import deque

custom_class = deque(maxlen=3)
custom_class.maxlen()
custom_class.append(1)
custom_class.append(2)
custom_class.append(3)
custom_class.popleft()
custom_class.clear()
custom_class.maxlen()