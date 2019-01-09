clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subnum,high_value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,mixed_value,mv_choosing_for_self,mv_self_choice1,mv_self_RT,mv_choosing_for_partner,mv_partner_choice1,mv_partner_RT,\n');

% participants ran with latest task code. 009 is our test code to make sure
% that everything works properly
sublist = [999];



for s = 1:length(sublist)
    
    subj = sublist(s);
    run = 1;
    
    tmp_data = zeros(run,1);
    for r = 1:run
        trial_data = "";
        %fname = fullfile(maindir,'psychopy','logs',num2str(subj),sprintf('sub-%03_partner_%03_task_b_results.csv',subj,r-1)); %creates variable to st|e the path to a given subject's data
        fname = "output/subject_999_partner_998_task_b_results.csv";
        fid = fopen(fname,'r+');
        %C = textscan(fid,(repmat('%f',1,13)),'Delimiter',',','HeaderLines',1); %creates a cell array C reading in the .csv file with the header rows
        C = textscan(fid,"%d %f %d %s %f %f %s %f %d %d %s %d %s",'Delimiter',',','HeaderLines',1);
        fclose(fid);
        whos C
        
        % omit computer responses - when adding new pc generated responses
        % check column 11 for 'n/a' as indicat|
        C(~strcmp(C(:,11),"n/a"),:);
        % C(C(:,12)~=1,:);
            
        % create variables for coding below
        Choice_1_RT = C{6};
        
        % run each line of each participant's output file through this code
        % items_value column (trial type)
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7
            high_value = C{1};
            strcat(trial_data,high_value,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8
            mixed_value = C{1};
            strcat(trial_data,mixed_value,"\t");
        end
        
        % choosing_for columns
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == self
            hv_choosing_for_self = C{13};
            strcat(trial_data,hv_choosing_for_self,"\t");
        end
        
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == partner
            hv_choosing_for_partner = C{13};
            strcat(trial_data,hv_choosing_for_partner,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == self
            mv_choosing_for_self = C{13};
            strcat(trial_data,mv_choosing_for_self,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == partner
            mv_choosing_for_partner = C{13};
            strcat(trial_data,mv_choosing_for_partner,"\t");
        end
        
        % Choice 1 columns
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == 1 % C{13} == 1 is choosing for self
            hv_self_choice1 = C{5};
            strcat(trial_data,hv_self_choice1,"\t");
        end
        
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == 2 % C{13} == 2 is choosing for partner
            hv_partner_choice1 = C{5};
            strcat(trial_data,hv_partner_choice1,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == 1
            mv_self_choice1 = C{5};
            strcat(trial_data,mv_self_choice1,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == 2
            mv_partner_choice1 = C{5};
            strcat(trial_data,mv_partner_choice1,"\t");
        end
        
        % Choice 1 RT columns
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == 1 % if high-value & choosing for self
            hv_choosing_self_RT = mean(Choice_1_RT);
            strcat(trial_data,hv_choosing_self_RT,"\t");
        end
        
        if C{1} == 1 | C{1} == 3 | C{1} == 5 | C{1} == 7 & C{13} == 2 % if high-value & choosing for partner
            hv_choosing_partner_RT = mean(Choice_1_RT);
            strcat(trial_data,hv_choosing_partner_RT,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == 1 % if mixed-value & choosing for self
            mv_choosing_self_RT = mean(Choice_1_RT);
            strcat(trial_data,mv_choosing_self_RT,"\t");
        end
        
        if C{1} == 2 | C{1} == 4 | C{1} == 6 | C{1} == 8 & C{13} == 2 % if mixed-value & choosing for partner
            mv_choosing_partner_RT = mean(Choice_1_RT);
            strcat(trial_data,mv_choosing_partner_RT,"\t");
        end
        % subnum,high-value,hv_choosing_for_self,hv_self_choice1,hv_self_RT,hv_choosing_for_partner,hv_partner_choice1,hv_partner_RT,mixed_value,mv_choosing_for_self
        % fprintf(fid_run,'%d,%f,%f,%f,%f,%f,%f,%f,%f\n;%d,%f,%f,%f,%f,%f,%f,%f,%f\n',subj);
        trial_data = trial_data(1:end-2);
        strcat(trial_data,"\n");
        % fprintf(fid_run,trial_data);
        fprintf(fid_run,'%d,%f,%f,%f,%f,%f,%f,%f,%f,%d,%f,%f,%f,%f,%f,%f,%f,%f\n',subj);
    end
    
    
end
fclose(fid_run);

