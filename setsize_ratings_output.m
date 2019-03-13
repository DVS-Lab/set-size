clear;
maindir = pwd;

% get participant output files
RatingsTask = dir('*_task_a_results.csv');
ChoiceTask = dir('*_task_b_results.csv');

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'snack_item,choosing_for_self,choosing_for_partner,\n');

sublist = [103 109 117];

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
    
    % define snack_item
    for i = 1:200(C{1})
        snack_item = % pull snack name from file namme (...\JOCN-master\task a\images\SNACKNAMES.jpg)
        % list each snack item in each row of the first column
    
    % once each snack has been listed:
    for i = 1:200(C{2})
        % take averages of each snack item pre-rating by looking at the second column of the Task A files for each participant
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

    % define ratings means
    choosing_for_self_means = [];
    choosing_for_partner_means = [];
    
    % pull choosing_for_self ratings data
    for i = 1:200(C{10})
        if isequal(C{12})(i),{'0'} % non-compuer responses
            if isequal(C{1}(i),{}) % trial types 
        % look for specific snack item
        % pull ratings data from C{10} and take averages across all participants
        
    
    % pull choosing_for_partner ratings data
    

end
