% SETSIZE_PRERATINGS_ZSCORES 
% This program:
% - reads all task b partipant data files
% - normalizes ratings (likert scale: 1-7) to z-score values
% - creates new output file to be used in main analysis script
%% Initialize
maindir = pwd;
output_folder_path = fullfile(maindir,'output');
sublist = [102];
%% Iterate through all participant files
% get participant output files
for s = 1:length(sublist)
    % Get subject ID
    subj_id = sublist(s);
    % Generate needed file name based on subj_id
    taskBFile = dir(fullfile(output_folder_path,...
        ['subject_' num2str(subj_id) '_partner*_task_b_results.csv']));

    % Open Participant's task B data file
    fname = taskBFile.name;
    input_file = fopen(fname);
    % Put data into cell struct
    task_b_data = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',');
    % Get relevant data
    snack_names = task_b_data(7);
    ratings = task_b_data(10);
    chosing_for = task_b_data(13);
    pc_response = task_b_data(12);
    TrialType = task_b_data(1);
    % Close task B data file
    fclose(input_file);

    % Format ratings to become double array
    ratings_temp = cellfun(@str2double,ratings{1:end},'UniformOutput',false);
    ratings_formatted = cell2mat(ratings_temp);
    % Normalize ratings to z-scores
    z_scores = normalize(ratings_formatted);
    
    % Format other data to double arrays
    chosing_for_temp = cellfun(@str2double,chosing_for{1:end},'UniformOutput',false);
    chosing_for_formatted = cell2mat(chosing_for_temp);
    pc_response_temp = cellfun(@str2double,pc_response{1:end},'UniformOutput',false);
    pc_response_formatted = cell2mat(pc_response_temp);
    % Format data to be written
    formatted_data = ...
        [TrialType{1:end} snack_names{1:end} num2cell(z_scores)...
        num2cell(chosing_for_formatted) num2cell(pc_response_formatted)];

    % Open output file
    % (file name is same as input file name but with '_formatted' appended)
    fname = fullfile(maindir,[taskBFile.name(1:end-4) '_z_scoresVK.csv']);
    output_file = fopen(fname,'w'); % csv uses commas (,) & tsv uses tabs (\t)
    % Write File Header
    fprintf(output_file,'snackName,rating,TrialType,choseFor,pcResponse\n');
    
    % write data line by line
    for i = 2:length(formatted_data)
        fprintf(output_file,'%s,%f,%d,%d,%d\n',formatted_data{i,:});
    end
    
    % Close output file
    fclose(output_file);
end
