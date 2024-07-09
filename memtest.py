import importlib
import sys
import resource

NUM_LISTS = 10**7

if len(sys.argv) == 2:
    module_name = sys.argv[1].replace('.py', '')
    module = importlib.import_module(module_name)
else:
    print('Usage: {} <linked-list-to-test>'.format())
    sys.exit(1)

fmt = 'Selected Linked_list type: {.__name__}.{.__name__}'
print(fmt.format(module, module.Linked_list))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} Linked_list instances'.format(NUM_LISTS))

linked_list = [module.Linked_list(20) for i in range(NUM_LISTS)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Initial RAM usage: {:14} MB'.format(mem_init/10**6))
print('Final RAM usage: {:14} MB'.format(mem_final/10**6))
