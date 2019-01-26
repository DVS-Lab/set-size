clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.tsv');
fid_run = fopen(fname,'w');
fprintf(fid_run,'subject_id\tChoosingForYou\tChoice1\tHighValue\tRT1\n');

% participants ran with latest task code. 009 is our test code to make sure
% that everything works properly
sublist = [999];

beginning_part = '999\t';
fname = 'output/subject_999_partner_998_task_b_results.csv';
fid = fopen(fname,'r');
for s = 1:length(sublist)
    
    subj = sublist(s);
    run = 180;
    
    choice1 = string.empty(0,run);
    
    %turns these values into 8-bit integers in the string
    highValue = int8.empty(0,run);
    
    % these are double.empty because the options are binary; they're either
    % 1 or 0
    you_high_RT = double.empty(0,run);
    partner_high_RT = double.empty(0,run);
    you_mixed_RT = double.empty(0,run);
    partner_mixed_RT = double.empty(0,run);
    
    %turns these values into 8-bit integers in the string
    choosing_for_vals = int8.empty(0,run);
    
    tmp_data = zeros(run,1);
    % run each line of each participant's output file through this code
    for r = 1:run
        trial_data = beginning_part;
        % fname = fullfile(maindir,'psychopy','logs',num2str(subj),sprintf('sub-%03_partner_%03_task_b_results.csv',subj,r-1)); %creates variable to st|e the path to a given subject's data
        C = textscan(fid,'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
        fclose(fid);
        
        % omit computer responses
        if C{12} == 0
            continue
        end
        
        % ChoosingForYou    
        if isequal(C{13},1)
            choosing_for_vals(r) = 1;
            % trial_data = strcat(trial_data,"1","\t");
        else
            choosing_for_vals(r) = 0;
            % trial_data = strcat(trial_data,"0","\t");
        end
        
        % Choice1
        choice = num2str(C{5});
        choice1(r) = choice(end);
        %trial_data = strcat(trial_data,num2str(C{5}),"\t");
                    
        % HighValue
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7
            highValue(r) = 1;
            if choosing_for_vals(r) == 1 % you choosing
                rt = C{6};
                you_high_RT(r) = rt(end);
            else 
                rt = C{6};
                partner_high_RT(r) = rt(end);
            end
            % trial_data = strcat(trial_data,"1","\t");
        else % is mixed value
            highValue(r) = 0; 
            if choosing_for_vals(r) == 1 % you choosing
                rt = C{6};
                you_mixed_RT(r) = rt(end);
            else 
                rt = C{6};
                partner_mixed_RT(r) = rt(end);
            end
            %trial_data = strcat(trial_data,"0","\t");
        end
            
        
        % fprintf(fid_run,trial_data(end));
        % fprintf(fid_run,'%d,%f,%f,%f,%f,%f,%f,%f,%f,%d,%f,%f,%f,%f,%f,%f,%f,%f\n',subj);
    end
    
end
fclose(fid_run);

