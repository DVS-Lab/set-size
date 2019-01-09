clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) and tsv uses tabs (\t)
fprintf(fid_run,'subnum,high_value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,\n subnum,mixed_value,mv_choosing_for_self,mv_self_choice1,mv_self_RT,mv_choosing_for_partner,mv_partner_choice1,mv_partner_RT,\n');

% participants ran with latest task code. 009 is our test code to make sure
% that everything works properly
sublist = [999]



for s = 1:length(sublist)
    
    subj = sublist(s);
    run = 1;
    
    tmp_data = zeros(run,1); % change 66 to 180 after example run. Our example was cut down to 66 runs.
    for r = 1:run
        %fname = fullfile(maindir,'psychopy','logs',num2str(subj),sprintf('sub-%03_partner_%03_task_b_results.csv',subj,r-1)); %creates variable to store the path to a given subject's data
        fname = "output/subject_999_partner_998_task_b_results.csv";
        fid = fopen(fname,'r+');
        %C = textscan(fid,(repmat('%f',1,13)),'Delimiter',',','HeaderLines',1); %creates a cell array C reading in the .csv file with the header rows
        C = textscan(fid,"%d %f %d %s %f %f %s %f %d %d %s %d %s",'Delimiter',',','HeaderLines',1);
        fclose(fid);
        whos C
        
        % omit computer responses - when adding new pc generated responses
        % check column 11 for 'n/a' as indicator
        C(~strcmp(C(:,11),"n/a"),:);
        % C(C(:,12)~=1,:);
            
        % create variables for coding below
        Choice_1_RT = C{6};
        
        % run each line of each participant's output file through this code
        % items_value column (trial type)
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7;
            then high_value == C{1};
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8;
            then mixed_value == C{1};
        end
        
        % choosing_for columns
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == self;
            then hv_choosing_for_self = C{13};
        end
        
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == partner;
            then hv_choosing_for_partner = C{13};
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == self;
            then mv_choosing_for_self = C{13};
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == partner;
            then mv_choosing_for_partner = C{13};
        end
        
        % Choice 1 columns
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == 1; % C{13} == 1 is choosing for self
            then hv_self_choice1 == C{5};
        end
        
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == 2; % C{13} == 2 is choosing for partner
            then hv_partner_choice1 == C{5};
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == 1;
            then mv_self_choice1 = C{5};
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == 2;
            then mv_partner_choice1 == C{5};
        end
        
        % Choice 1 RT columns
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == 1; % if high-value and choosing for self
            then hv_choosing_self_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 1 or C{1} == 3 or C{1} = 5 or C{1} == 7, and C{13} == 2; % if high-value and choosing for partner
            then hv_choosing_partner_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == 1; % if mixed-value and choosing for self
            then mv_choosing_self_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 2 or C{1} == 4 or C{1} == 6 or C{1} == 8, and C{13} == 2 % if mixed-value and choosing for partner
            then mv_choosing_partner_RT == mean(Choice_1_RT);
        end
        
    end
    % subnum,high-value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,mixed_value,mv_choosing_for_self
    fprintf(fid_run,'%d,%f,%f,%f,%f,%f,%f,%f,%f\n;%d,%f,%f,%f,%f,%f,%f,%f,%f\n',subj);
    
end
fclose(fid_run);

