%% note that we are excluding monetary selections for these analyses
%% working off of setsize_revalRatings_zScores.m to write this

clear;
maindir = pwd;

% Get task B data
taskBFile = dir('*_task_b_results_z_scores_tt.csv'); % make sure these files are in the main directory. I'll fix this later, but for now we're just putting that stuff here.

% open output files
fname = fullfile(maindir,'setsize_revalRatings_zScores_pval_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,choosingFor,setValue,setSize,revalRating\n');

sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];

for s = 1:length(taskBFile)   
    subj_id = sublist(s);
    file_name = taskBFile(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',');
    fclose(fid);
    
    trial_data = '';

    choosingFor = C(7);
    
    
    setValue = C(
    if trial type is 1 % you_high
        if set size is 2
            choosingFor is you
            setValue is high
            setSize is 2
            revalRating goes in that row % this will get written into a string that the average will be taken from
        elseif set size is 3
            choosingFor is you
            setValue is high
            setSize is 3
            revalRating goes in that row
        elseif set size is 6
            choosingFor is you
            setValue is high
            setSize is 6
            revalRating goes in that row
        elseif set size is 12
            choosingFor is you
            setValue is high
            setSize is 2
            revalRating goes in that row
    if trial type is 2 % you_mixed
        if set size is 2
            choosingFor is you
            setValue is mixed
            setSize is 2
            revalRating goes in that row
        elseif set size is 3
            choosingFor is you
            setValue is mixed
            setSize is 3
            revalRating goes in that row
        elseif set size is 6
            choosingFor is you
            setValue is mixed
            setSize is 6
            revalRating goes in that row
        elseif set size is 12
            choosingFor is you
            setValue is mixed
            setSize is 2
            revalRating goes in that row
    
            
            
            
            
    % define columns
    for i = length(C{1})
        if isequal(
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    % write in tmp_data
    tmp_data = [subj_id choosingFor setValue setSize revalRating];

    % write data to output file 'setsize_revalRatings_zScores_output.csv'
    fprintf(fid_run,'%s,%s,%s,%s,%s\n',tmp_data);
end
fclose(fid_run);
