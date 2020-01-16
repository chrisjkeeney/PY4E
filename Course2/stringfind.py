text = "X-DSPAM-Confidence:    0.8475";

number = text.find('0')
number = text[number:]
n = float(number)
print(n)
