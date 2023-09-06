import yaml
import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='File Path Parser')
parser.add_argument('bag_path', type=str, help='Path to the file')
parser.add_argument('num_iterations', type=int, help='How often each setup')
args = parser.parse_args()
bag_path = args.bag_path
num_iterations = args.num_iterations

setup_ctr = 0

with open('files_for_testing/param_setups.txt', 'r') as file:
    for line in file:
        line_split = line.split()

        setup_ctr = setup_ctr + 1

        # Open the YAML file for reading
        with open('src/SC-LIO-SAM/SC-LIO-SAM/config/params_liosam.yaml', 'r') as file:
        # Load the YAML data into a Python dictionary
            data = yaml.safe_load(file)

        # Modify some parameters in the YAML data 17 Parameter
        #LoopClosure Parameter
        data['loopClosureFrequency'] = line_split[0] 
        data['surroundingKeyframeSize'] = line_split[1] # WIRD NICHT GENUTZT
        data['historyKeyframeSearchRadius'] = line_split[2]
        data['historyKeyframeSearchTimeDiff'] = line_split[3] 
        data['historyKeyframeSearchNum'] = line_split[4] 
        data['historyKeyframeFitnessScore'] = line_split[5]
        #Keyframe Parameter
        data['surroundingkeyframeAddingDistThreshold'] = line_split[6] 
        data['surroundingkeyframeAddingAngleThreshold'] = line_split[7]
        data['surroundingKeyframeDensity'] = line_split[8] 
        data['surroundingKeyframeSearchRadius'] = line_split[9]
        #Voxel Filter Parameter
        data['odometrySurfLeafSize'] = line_split[10] 
        data['mappingCornerLeafSize'] = line_split[11] 
        data['mappingSurfLeafSize'] = line_split[12]
        #LOAM feature threshold
        data['edgeThreshold'] = line_split[13] 
        data['surfThreshold'] = line_split[14]
        data['edgeFeatureMinValidNum'] = line_split[15] 
        data['surfFeatureMinValidNum'] = line_split[16]

        # Open the YAML file for writing
        with open('src/SC-LIO-SAM/SC-LIO-SAM/config/params_liosam.yaml', 'w') as file:
        # Dump the modified YAML data back to the file
            yaml.dump(data, file)

        #subprocesses callen, bash script, das alles startet und aufnahme startet
        LC = "{}_{}_{}_{}_{}_{}".format(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4], line_split[5])
        KF = "{}_{}_{}_{}".format(line_split[6], line_split[7], line_split[8], line_split[9])
        VF = "{}_{}_{}".format(line_split[10], line_split[11], line_split[12])
        LF = "{}_{}_{}_{}".format(line_split[13], line_split[14], line_split[15], line_split[16])
        
        for i in range(num_iterations):
            setup_str = str(setup_ctr)
            iter_str = str(i)
            filename = "SETUP_{}_ITER_{}_LC_{}_KF_{}_VF_{}_LF_{}".format(setup_str, iter_str, LC, KF, VF, LF)

            subprocess.run(['files_for_testing/start_lio_sam.sh', bag_path, filename])
            time.sleep(10)
            subprocess.run(['files_for_testing/bag_to_csv.sh', filename])