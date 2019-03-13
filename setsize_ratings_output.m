clear;
maindir = pwd;

% get participant output files
RatingsTask = dir('*_task_a_results.csv');
ChoiceTask = dir('*_task_b_results.csv');

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,INSERTSTUFFHERE\n');

sublist = [102 109 110 111 113 115 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134];

% pulling from Ratings Task--------------------------------------------------------------------------------
for s = 1:200(RatingsTask)
    subj_id = sublist(s);
    file_name = RatingsTask(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output files
    C = textscan(fopen(fname,'r'),'%s,%s,%s','Delimiter',',');
    fclose(fid);
    
    trial_data = '';
    
    % put more here
    

end

% pulling from Choice Task---------------------------------------------------------------------------------
for s = 1:length(ChoiceTask)   
    subj_id = sublist(s);
    file_name = ChoiceTask(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);

    trial_data = '';



end
