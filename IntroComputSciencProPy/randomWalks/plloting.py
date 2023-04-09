#import pylab 
import drunkUsual as drunkClass
import iteringStyles as st
import driver
import matplotlib.pyplot as pylab
def sim_drunk(num_trials, d_class, walk_lengths):
    print(d_class.__name__)
    meanDistances = []
    for num_steps in walk_lengths:
        print('Starting simulatio of ', num_steps, 'steps')
        trials = driver.simWalks(num_steps, num_trials,d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    print(meanDistances)
    return meanDistances

def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    styles_choice = st.style_iterator(('m-','r:','k-.'))
    for d_class in drunk_kinds:
        curt_style = styles_choice.nextStyle()
        print('Starting simulatio of ', d_class.__name__)
        means = sim_drunk(num_trials, d_class,walk_lengths)
        pylab.plot(walk_lengths, means, curt_style, label = d_class.__name__)
    pylab.title(f'Mean Distance from Origin({num_trials})')
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

sim_all_plot((drunkClass.UsualDrunk,drunkClass.Cold_drunk,drunkClass.EW_drunk),(3,10,100,1000,10000,100000),10)
