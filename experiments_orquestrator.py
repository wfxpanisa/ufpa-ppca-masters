#!/usr/bin/python3

import subprocess

first_timer = '5'
second_timer = '3'
logging_timer = '16'
no_logging = '0'

base_path = '/home/victor/Coding/msc_exp'
script_path = '/'.join([base_path, 'preload_script.sh'])
out_path = '/'.join(['/opt/', 'experiment_output'])
preload_lib_path = '/'.join([base_path, 'debug_malloc.so'])
temp_storage_path = '/'.join([base_path, 'temp_storage.dat'])
app_list_file_path = '/'.join([base_path, 'app_list.txt'])

amount_test_iterations = 30


def read_app_list_file(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def run_shell_command(cmd):
    return subprocess.run(cmd, shell=True, universal_newlines=True, capture_output=True)


def read_temp_storage():
    with open(temp_storage_path, 'r') as f:
        return int(f.readline().splitlines()[0])


def run_experiment(app_name):
    app_path = '/'.join([out_path, app_name])
    run_shell_command('mkdir -p {}'.format(app_path))
    run_shell_command('rm /tmp/*.csv')
    run_shell_command('rm {}/*'.format(app_path))
    subprocess.run([script_path, app_name, preload_lib_path, first_timer, no_logging])
    for i in range(amount_test_iterations):
        subprocess.run(
            [script_path, app_name, preload_lib_path, second_timer, logging_timer]
        )
        for csv_base_name in ['malloc', 'free']:
            origin_csv_full_path = run_shell_command('ls /tmp/{}*.csv'.format(csv_base_name)).stdout.splitlines()
            if len(origin_csv_full_path) > 0:
                origin_csv_full_path = origin_csv_full_path[0]
                destination_csv_full_path = '/'.join(
                    [app_path, '-'.join([csv_base_name, app_name, str(i + 1) + '.csv'])])
                run_shell_command(' '.join(['mv', origin_csv_full_path, destination_csv_full_path]))


def main():
    current_exp_index = read_temp_storage()
    if current_exp_index == -1:  # not running
        pass
    else:
        app_config_list = read_app_list_file(app_list_file_path)
        run_experiment(app_config_list[read_temp_storage()])
        current_exp_index += 1
        if current_exp_index == len(app_config_list):
            current_exp_index = -1
        with open(temp_storage_path, "w") as text_file:
            print(current_exp_index, file=text_file)
        run_shell_command('/sbin/reboot')


if __name__ == '__main__':
    main()
