from datetime import datetime
from time import sleep

from playsound import playsound



def count(to=11):
	for i in range(1, to):
		# sleep(1)
		playsound(f'sounds/{i}.wav')



def run(sets=3, reps=11):
	# sleep(5)
	set_counter = sets

	while set_counter > 0:
		count(reps)
		# sleep(2	)
		set_counter -= 1

	return sets, reps-1


def write_log(filename="log.csv", data=''):
	with open(filename, "a") as log_file:
		log_file.write(data)



def main():
	exercise = input("Exercise Name: ")
	now = datetime.now()
	f_now = now.strftime("%d-%m-%Y,%H:%M:%S")
	
	sets, reps = run(3)
	
	s = f"{f_now},{exercise},{sets}x{reps},{sets * reps}\n"
	write_log(data=s)



if __name__ == '__main__':
	main()
