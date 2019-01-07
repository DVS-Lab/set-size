clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) and tsv uses tabs (\t)
fprintf(fid_run,'subnum,high_value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,\n;subnum,mixed_value,mv_choosing_for_self,mv_self_choice1,mv_self_RT,mv_choosing_for_partner,mv_partner_choice1,mv_partner_RT,\n');

% participants ran with latest task code. 009 is our test code to make sure
% that everything works properly
sublist = [009]



for s = 1:length(sublist)
    
    subj = sublist(s);
    runs = 1;
    
    tmp_data = zeros(run,66); % change 66 to 180 after example run. Our example was cut down to 66 runs.
    for r = 1:runs
        fname = fullfile(maindir,'psychopy','logs',num2str(subj),sprintf('sub-%03_partner_%03_task_b_results.csv',subj,r-1)); %creates variable to store the path to a given subject's data
        fid = fopen(fname,'r');
        C = textscan(fid,(repmat('%f',1,14)),'Delimiter',',','HeaderLines',1,'EmptyValue',NaN); %creates a cell array C reading in the .csv file with the header rows
        fclose(fid);
        
        % omit computer responses
        C(C(:,12)~=1,:);
            
        % create variables for coding below
        Choice_1_RT = C{6};
        
        % run each line of each participant's output file through this code
        % items_value column (trial type)
        if C{1} == 1;
            then high_value == C{1};
        end
        
        if C{1} == 2;
            then mixed_value == C{1};
        end
        
        % choosing_for columns
        if C{1} == 1, and C{13} == self;
            then hv_choosing_for_self = C{13};
        end
        
        if C{1} == 1, and C{13} == partner;
            then hv_choosing_for_partner = C{13};
        end
        
        if C{1} == 2, and C{13} == self;
            then mv_choosing_for_self = C{13};
        end
        
        if C{1} == 2, and C{13} == partner;
            then mv_choosing_for_partner = C{13};
        end
        
        % Choice 1 columns
        if C{1} == 1, and C{13} == self;
            then hv_self_choice1 == C{5};
        end
        
        if C{1} == 1, and C{13} == partner;
            then hv_partner_choice1 == C{5};
        end
        
        if C{1} == 2, and C{13} == self;
            then mv_self_choice1 = C{5};
        end
        
        if C{1} == 2, and C{13} == partner;
            then mv_partner_choice1 == C{5};
        end
        
        % Choice 1 RT columns
        if C{1} == 1, and C{13} == self; % if high-value and choosing for self
            then hv_choosing_self_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 1, and C{13} == partner; % if high-value and choosing for partner
            then hv_choosing_partner_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 2, and C{13} == self; % if mixed-value and choosing for self
            then mv_choosing_self_RT == mean(Choice_1_RT);
        end
        
        if C{1} == 2, and C{13} == partner % if mixed-value and choosing for partner
            then mv_choosing_partner_RT == mean(Choice_1_RT);
        end
        
    end
    % subnum,high-value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,mixed_value,mv_choosing_for_self
    fprintf(fid_subj,'%d,%f,%f,%f,%f,%f,%f,%f,%f\n;%d,%f,%f,%f,%f,%f,%f,%f,%f\n',subj);
    
end
fclose(fid_run);
