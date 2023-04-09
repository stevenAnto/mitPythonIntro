import drunkUsual as drunkClass
import iteringStyles as st
import driver
import matplotlib.pyplot as plt
def sim_drunk(num_trials, d_class, walk_lengths):
    meanDistances = []
    for num_steps in walk_lengths:
        print('Starting simulatio of ', num_steps, 'steps')
        trials = driver.simWalks(num_steps, num_trials,d_class)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def sim_all_plot(drunk_kinds, walk_lengths, num_trials):
    styles_choice = st.style_iterator(('m-','r:','k-.'))
    for d_class in drunk_kinds:
        curt_style = styles_choice.nextStyle()
        print('Starting simulatio of ', d_class.__name__)
        means = sim_drunk(num_trials, d_class,walk_lengths)
        plt.plot(walk_lengths, means, curt_style, label = d_class.__name__)
    plt.title(f'Mean Distance from Origin({num_trials})')
    plt.xlabel('Number of Steps')
    plt.ylabel('Distance from Origin')
    plt.legend(loc='best')
    plt.semilogx()
    plt.semilogy()

sim_all_plot((drunkClass.UsualDrunk,drunkClass.Cold_drunk,drunkClass.EW_drunk),(10,100,1000,10000,100000),100)
