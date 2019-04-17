% SETSIZE_RATINGS_OUTPUT
% This program:
% - Loads in z-score converted task a & b data
% - averages the z-scores for each snack item across all participants

%% Initalize
% Get main directory path
main_dir_path = pwd;
% List subject ID's
sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];
output_z_score_folder_path = fullfile(main_dir_path,'output_z_scores');
% Initalize all subject data
pre_rating_means_all = [];
you_means_all = [];
partner_means_all = [];
%% Get Images
snack_image_files = dir('images/*.jpg');
snack_names = {};

for i = 1:length(snack_image_files)
    [~,name,~] = fileparts(snack_image_files(i).name);
    snack_names{end+1} = name;
end
%% Iterate thrrough each participant
for subject = sublist
    % Initalize single subject only data
    subject_pre_ratings = [];
    subject_you_ratings = [];
    subject_partner_ratings = [];
    
    % Get task a data
    task_a_file = dir(fullfile(output_z_score_folder_path,...
        [num2str(subject) '_task_a_results_z_scores.csv']));

    file_name = task_a_file.name;
    fid_task_a = fopen(file_name);
    task_a_data = textscan(fopen(file_name,'r'),'%s%s','Delimiter',',');
    fclose(fid_task_a);
    
    %% Iterate through each snack item
    % Get pre-rating z-scores from task a
    for i = 1:length(snack_names)
        % ReInitalize for every snack type
        snack_rating = [];
        %% Iterate through each participant choice
        for j = 1:length(task_a_data{1,1}) % Iterate through all choices
           [~,snack_name,~] = fileparts(task_a_data{1}{j});
           if isequal(snack_names{i},snack_name) % choice is current snack
              snack_rating = [snack_rating, task_a_data{2}(j)];
           end
        end
        subject_pre_ratings = [subject_pre_ratings, snack_rating];
    end
    pre_rating_means_all = [pre_rating_means_all; subject_pre_ratings];
    
    % Get task b data
    task_b_file = dir(fullfile(output_z_score_folder_path,...
        ['subject_' num2str(subject) '_partner*_task_b_results_z_scores.csv']));
    file_name = task_b_file.name;
    fid_task_b = fopen(file_name);
    task_b_data = textscan(fopen(file_name,'r'),'%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid_task_b);
    
    %% Iterate through each snack item
    % Get you and partner rating z-scores from task b data
    for i = 1:length(snack_names) % for all snack names
        % ReInitalize for every snack type
        rating_you = [];
        rating_partner = [];
        %% Iterate through each participant choice
        for j = 1:length(task_b_data{1,1}) % Iterate through all choices
           % Get snack name
           [~,snack_name,~] = fileparts(task_b_data{1}{j});
           % Check if jth snack name matches snack_name at ith index
           if isequal(snack_names{i},snack_name) % choice is current snack
               % Filter out computer responses
               if isequal(task_b_data{4}{j}, '0') % is participant response
                  % Get ratings (You or Partner)
                  if task_b_data{3}{j} == '1' % Chose for self
                    rating_you = [rating_you, str2double(task_b_data{2}{j})];
                  else % Chose for parner
                    rating_partner = [rating_partner,...
                        str2num(task_b_data{2}{j})]; % consider str2fdouble********
                  end
               end
           end
        end
        subject_you_ratings = [subject_you_ratings, nanmean(rating_you)];
        subject_partner_ratings = [subject_partner_ratings, nanmean(rating_partner)];
    end
    you_means_all = [you_means_all; subject_you_ratings];
    partner_means_all = [partner_means_all; subject_partner_ratings];
    fclose('all');
end

 %% Data formatting

% transpose from 1xn to nx1 
snack_names = snack_names';
% convert str to double
pre_rating_means_all_temp = cellfun(@str2double,pre_rating_means_all,'UniformOutput',false);
% convert cell array to double array
pre_rating_means_formatted = cell2mat(pre_rating_means_all_temp);

%% Get Means 
% get mean of participant
pre_rating_means = nanmean(pre_rating_means_formatted)';
you_means_all = nanmean(you_means_all)';
partner_means_all = nanmean(partner_means_all)';
%% Write Data to Output File
% Arrange data for writing
formatted_data = [snack_names, num2cell(pre_rating_means),...
    num2cell(you_means_all), num2cell(partner_means_all)];

% Create output file
file_name = fullfile(main_dir_path,'setsize_ratings_output.csv');
fid_output = fopen(file_name,'w'); % csv uses commas (,) & tsv uses tabs (\t)
% Write header
fprintf(fid_output,'snack_name,preRatingMean,youRatingMean,partnerRatingMean\n');
% write data to output file 'setsize_ratings_output.tsv'
for i = 1:length(formatted_data)
    fprintf(fid_output,'%s,%f,%f,%f\n',formatted_data{i,:});
end
fclose(fid_output);