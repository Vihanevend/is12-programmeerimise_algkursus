print ("{:,}".format(2500000));
print ("{:.2f}".format(17.22331));
print ("{:+.2f}".format(-47));
print ("{:.0f}".format(12.34345));
print #
print'{0}, {1}, {2}'.format('a', 'b', 'c')
print'{2}, {1}, {0}'.format('a', 'b', 'c')
print'{0}, {1}, {2}'.format(*'abc')
print'{0}{1} ,{0}{1}'.format('mets' , 'jeesus')
print #
print'Coordinates: {latitude}, {longitude}'.format(latitude='52.15S', longitude='-142.14E')

koord = {'latitude' : '123.213N' , 'longitude' : '28.23W'}
print'Coordinates: {latitude}, {longitude}'.format(**koord)
print #
kord= 24,71
print'X: {0[0]};  Y: {0[1]}'.format(kord)
print #
points = 16.5
total = 22
print'Correct answers: {0:.2%}.'.format(points/total)
