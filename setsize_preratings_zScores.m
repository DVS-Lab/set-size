% SETSIZE_PRERATINGS_ZSCORES 
% This program:
% - reads all task a partipant data files
% - normalizes participant ratings (likert scale: 1-7) to z-score values.
%% Initialize
maindir = pwd;
output_folder_path = fullfile(maindir,'output');
sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];
%% Iterate through all participant files
% get participant output files
for s = 1:length(sublist)
    % Get subject ID
    subj_id = sublist(s);
    % Generate needed file name based on subj_id
    task_a_file = dir(fullfile(output_folder_path,[num2str(subj_id) '_task_a_results.csv']));
    
    % Open Participant's taskA data file
    file_name = task_a_file.name;
    input_file = fopen(file_name);
    % Put data into cell struct
    task_a_data = textscan(fopen(file_name,'r'),'%s%d%d','Delimiter',',');
    % Get relevant data
    snack_names = task_a_data(1);
    ratings = cell2mat(task_a_data(2));
    % Close taskA data file
    fclose(input_file);
    
    % Normalize ratings to z-scores
    ratings = double(ratings);
    z_scores = zscore(ratings);
    
    % Format data to be written
    formatted_data = [snack_names{1:end} num2cell(z_scores)];

    % Open output file
    % (file name is same as input file name but with '_formatted' appended)
    file_name = fullfile(maindir,[num2str(subj_id) '_task_a_results_z_scores.csv']);
    output_file = fopen(file_name,'w'); % csv uses commas (,) & tsv uses tabs (\t)
    % Write File Header
    fprintf(output_file,'subj_id,zScore\n');
    
    % write data line by line
    for i = 1:length(formatted_data)
        fprintf(output_file,'%s,%f\n',formatted_data{i,:});
    end
    
    % Close output file
    fclose(output_file);

end
