import os
import sys
import pygame
import subprocess
import time

# initialize the pygame environment, which we use to display an image
def init():
	global screen

	# unused
	#global procID
	#procID = 0
	
	# seetup mygame enviornment
	pygame.init()
	screen = pygame.display.set_mode((0,0))
	pygame.mouse.set_visible(0)
	screen.fill((255,0,0))
	
	# plays first file on drive
	filename = getVidFile()
	if fileName == None:
		print "no video files on drive, exiting"
	else:
		playVideo('trvloop_full.mp4')


# exit loop on keydown
def loop():
	# unused code
	#global screen
	#global procID
	#global process

	loop = True
	while loop:
		# grab keyboard event, if keydown we break out of loop (good for testing)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				# spacebar will kill the process
				if event.key == pygame.K_SPACE:
					loop = False
					os.system('killall omxplayer.bin')
		
		# not working loop code
		#		elif event.key == pygame.K_2:
		#			playVideo('sonydcrtrv700-digital8.mp4')
		
		# do other things in loop	
		# not working code
		#if pid_exists(procID) == False:
		#	fileWrite("finished")
		#	playVideo('sonydcrtrv700-digital8.mp4')

		time.sleep(1)	
	#loop = False

		

def getVidFile():
	filename = "trvloop_full.mp4"
	return filename


# open a subprocess which will look omxplayer
# omxplayer has an annoying loop message, so make your loop 30 min long to minimize the damaage
def playVideo(filename):
	global procID
	process = subprocess.Popen(['omxplayer','--loop','usbdrv/vids/' + filename])
	procID = process.pid
	fileWrite("omxplayer proc ID = " + str(procID))


# simple append-to-file logger, change type do "a"
# now, it is a one-line file-logger	
def fileWrite(line):
	f = open("log.txt","w")
	f.write(line)
	f.write("\n")
	f.close()
	

init()
loop()


# procID code (not used)

#def pid_exists(pid):
    #Check whether pid exists in the current process table. UNIX only.
    
#    if pid < 0:
#        return False
#    if pid == 0:
        # According to "man 2 kill" PID 0 refers to every process
        # in the process group of the calling process.
        # On certain systems 0 is a valid PID but we have no way
        # to know that in a portable fashion.
#        raise ValueError('invalid PID 0')
#    try:
#        os.kill(pid, 0)
#    except OSError as err:
 #       if err.errno == errno.ESRCH:
            # ESRCH == No such process
#            return False
#        elif err.errno == errno.EPERM:
            # EPERM clearly means there's a process to deny access to
#            return True
#        else:
            # According to "man 2 kill" possible error values are
            # (EINVAL, EPERM, ESRCH)
#            raise
#    else:
#        return True



#def getProcID(processName):
#        proc = subprocess.Popen(['pidof',processName], stdout=subprocess.PIPE)
#        text = proc.communicate()[0].decode('utf-8')
#	print(text)
#        pID = int(text)
#        return pID
