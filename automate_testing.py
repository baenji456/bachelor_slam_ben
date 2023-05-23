import yaml
import subprocess
import time

# TODO argparse für abzuspielendes bagfile

with open('param_setups.txt', 'r') as file:
    for line in file:
        line_split = line.split()

        # Open the YAML file for reading
        with open('src/SC-LIO-SAM/SC-LIO-SAM/config/params_liosam.yaml', 'r') as file:
        # Load the YAML data into a Python dictionary
            data = yaml.safe_load(file)

        # Modify some parameters in the YAML data 17 Parameter
        #LoopClosure Parameter
        data['loopClosureFrequency'] = line_split[0] 
        data['surroundingKeyframeSize'] = line_split[1] 
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

        filename = "LC_{}_KF_{}_VF_{}_LF_{}".format(LC, KF, VF, LF)

        subprocess.run(['./start_lio_sam.sh', "labor_klein.bag", filename])
        time.sleep(10)
        subprocess.run(['./bag_to_csv.sh', filename])