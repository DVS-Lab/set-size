clear;
maindir = pwd;

% get participant output files
RatingsTask = dir('*_task_a_results.csv');
ChoiceTask = dir('*_task_b_results.csv');

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'snack_item,pre_ratings_means,choosing_for_self_means,choosing_for_partner_means,\n');

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
    
    % define ratings means
    pre_ratings_means = [];
    
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
    choosing_for_self_high_means = [];
    choosing_for_self_mixed_means = [];
    choosing_for_self_means = [];
    choosing_for_partner_high_means = [];
    choosing_for_partner_mixed_means = [];
    choosing_for_partner_means = [];
    
    % look for specific snack item
    for i = 1:200
        if isequal(C{7}(i),{STRING?}) % do I need to define each snack item whose ratings I'm grabbing??
    
    % pull choosing_for_self ratings data
    for i = 1:length(C{12})
        if isequal(C{12}(i),{'0'} % non-compuer responses
            if % a snack item is selected in C{7} % could be written as a string being selected maybe?
                if isequal(C{1}(i),{'1'}) % you_high
                    choosing_for_self_high = str2double(C{10}(i));
                    choosing_for_self_high_means = [choosing_for_self_high_means,choosing_for_self_high];
                if isequal(C{1}(i),{'2'}) % you_mixed
                    choosing_for_self_mixed = str2double(C{10}(i));
                    choosing_for_self_mixed_means = [choosing_for_self_mixed_means,choosing_for_self_mixed];
                if isequal(C{1}(i),{'5'}) % partner_high
                    choosing_for_partner_high = str2double(C{10}(i);
                    choosing_for_partner_high_means = [choosing_for_partner_high_means,choosing_for_partner_high];
                if isequal(C{1}(i),{'6'}) % partner_mixed
                    choosing_for_partner_mixed = str2double(C{10}(i));
                    choosing_for_partner_mixed_means = [choosing_for_partner_mixed_means,choosing_for_partner_mixed];
            choosing_for_self_means = [choosing_for_self_means,choosing_for_self_high_means,choosing_for_self_mixed_means];
            choosing_for_partner_means = [choosing_for_partner_means,choosing_for_partner_high_means,choosing_for_partner_mixed_means];
        
    % pull choosing_for_partner ratings data
    
end
