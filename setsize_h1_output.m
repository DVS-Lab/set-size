clear;
maindir = pwd;

% get participant output files
myFiles = dir('*results.csv');

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,you_high2RT_mean,you_high3RT_mean,you_high6RT_mean,you_high12RT_mean,you_highmonRT_mean,you_mixed2RT_mean,you_mixed3RT_mean,you_mixed6RT_mean,you_mixed12RT_mean,you_mixedmonRT_mean,partner_high2RT_mean,partner_high3RT_mean,partner_high6RT_mean,partner_high12RT_mean,partner_highmonRT_mean,partner_mixed2RT_mean,partner_mixed3RT_mean,partner_mixed6RT_mean,partner_mixed12RT_mean,partner_mixedmonRT_mean\n');

sublist = [102 109 110 111 113 115 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134];

for s = 1:length(myFiles)   
    subj_id = sublist(s);
    file_name = myFiles(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);

    trial_data = '';

    % define you_high means
    you_high2RT_means = [];
    you_high3RT_means = [];
    you_high6RT_means = [];
    you_high12RT_means = [];
    you_highmonRT_means = [];

    % define you_mixed means
    you_mixed2RT_means = [];
    you_mixed3RT_means = [];
    you_mixed6RT_means = [];
    you_mixed12RT_means = [];
    you_mixedmonRT_means = [];

    % define partner_high means
    partner_high2RT_means = [];
    partner_high3RT_means = [];
    partner_high6RT_means = [];
    partner_high12RT_means = [];
    partner_highmonRT_means = [];

    % define partner_mixed means
    partner_mixed2RT_means = [];
    partner_mixed3RT_means = [];
    partner_mixed6RT_means = [];
    partner_mixed12RT_means = [];
    partner_mixedmonRT_means = [];

    % defines RT's
    for i = 1:length(C{12})
        if isequal(C{12}(i),{'0'}) % non-computer responses
            if isequal(C{1}(i),{'1'}) % you_high
                if isequal(C{5}(i),{'2'}) % set size 2
                    you_high2RT = str2double(C{6}(i));
                    you_high2RT_means = [you_high2RT_means,you_high2RT];
                elseif isequal(C{5}(i),{'3'}) % set size 3
                    you_high3RT = str2double(C{6}(i));
                    you_high3RT_means = [you_high3RT_means,you_high3RT];
                elseif isequal(C{5}(i),{'6'}) % set size 6
                    you_high6RT = str2double(C{6}(i));
                    you_high6RT_means = [you_high6RT_means,you_high6RT];
                elseif isequal(C{5}(i),{'12'}) % set size 12
                    you_high12RT = str2double(C{6}(i));
                    you_high12RT_means = [you_high12RT_means,you_high12RT];
                else % monetary values
                    you_highmonRT = str2double(C{6}(i));
                    you_highmonRT_means = [you_highmonRT_means,you_highmonRT];
                end
            end
            if isequal(C{1}(i),{'2'}) % you_mixed
                if isequal(C{5}(i),{'2'}) % set size 2
                    you_mixed2RT = str2double(C{6}(i));
                    you_mixed2RT_means = [you_mixed2RT_means,you_mixed2RT];
                elseif isequal(C{5}(i),{'3'}) % set size 3
                    you_mixed3RT = str2double(C{6}(i));
                    you_mixed3RT_means = [you_mixed3RT_means,you_mixed3RT];
                elseif isequal(C{5}(i),{'6'}) % set size 6
                    you_mixed6RT = str2double(C{6}(i));
                    you_mixed6RT_means = [you_mixed6RT_means,you_mixed6RT];
                elseif isequal(C{5}(i),{'12'}) % set size 12
                    you_mixed12RT = str2double(C{6}(i));
                    you_mixed12RT_means = [you_mixed12RT_means,you_mixed12RT];
                else % monetary values
                    you_mixedmonRT = str2double(C{6}(i));
                    you_mixedmonRT_means = [you_mixedmonRT_means,you_mixedmonRT];
                end
            end
            if isequal(C{1}(i),{'5'}) % partner_high
                if isequal(C{5}(i),{'2'}) % set size 2
                    partner_high2RT = str2double(C{6}(i));
                    partner_high2RT_means = [partner_high2RT_means,partner_high2RT];
                elseif isequal(C{5}(i),{'3'}) % set size 3
                    partner_high3RT = str2double(C{6}(i));
                    partner_high3RT_means = [partner_high3RT_means,partner_high3RT];
                elseif isequal(C{5}(i),{'6'}) % set size 6
                    partner_high6RT = str2double(C{6}(i));
                    partner_high6RT_means = [partner_high6RT_means,partner_high6RT];
                elseif isequal(C{5}(i),{'12'}) % set size 12
                    partner_high12RT = str2double(C{6}(i));
                    partner_high12RT_means = [partner_high12RT_means,partner_high12RT];
                else % monetary values
                    partner_highmonRT = str2double(C{6}(i));
                    partner_highmonRT_means = [partner_highmonRT_means,partner_highmonRT];
                end
            end
            if isequal(C{1}(i),{'6'}) % partner_mixed
                if isequal(C{5}(i),{'2'}) % set size 2
                    partner_mixed2RT = str2double(C{6}(i));
                    partner_mixed2RT_means = [partner_mixed2RT_means,partner_mixed2RT];
                elseif isequal(C{5}(i),{'3'}) % set size 3
                    partner_mixed3RT = str2double(C{6}(i));
                    partner_mixed3RT_means = [partner_mixed3RT_means,partner_mixed3RT];
                elseif isequal(C{5}(i),{'6'}) % set size 6
                    partner_mixed6RT = str2double(C{6}(i));
                    partner_mixed6RT_means = [partner_mixed6RT_means,partner_mixed6RT];
                elseif isequal(C{5}(i),{'12'}) % set size 12
                    partner_mixed12RT = str2double(C{6}(i));
                    partner_mixed12RT_means = [partner_mixed12RT_means,partner_mixed12RT];
                else % monetary values
                    partner_mixedmonRT = str2double(C{6}(i));
                    partner_mixedmonRT_means = [partner_mixedmonRT_means,partner_mixedmonRT];
                end
            end
        end
    end

    % find you_high means
    you_high2RT_mean = mean(you_high2RT_means);
    you_high3RT_mean = mean(you_high3RT_means);
    you_high6RT_mean = mean(you_high6RT_means);
    you_high12RT_mean = mean(you_high12RT_means);
    you_highmonRT_mean = mean(you_highmonRT_means);

    % find you_mixed means
    you_mixed2RT_mean = mean(you_mixed2RT_means);
    you_mixed3RT_mean = mean(you_mixed3RT_means);
    you_mixed6RT_mean = mean(you_mixed6RT_means);
    you_mixed12RT_mean = mean(you_mixed12RT_means);
    you_mixedmonRT_mean = mean(you_mixedmonRT_means);

    % find partner_high means
    partner_high2RT_mean = mean(partner_high2RT_means);
    partner_high3RT_mean = mean(partner_high3RT_means);
    partner_high6RT_mean = mean(partner_high6RT_means);
    partner_high12RT_mean = mean(partner_high12RT_means);
    partner_highmonRT_mean = mean(partner_highmonRT_means);

    % find partner_mixed means
    partner_mixed2RT_mean = mean(partner_mixed2RT_means);
    partner_mixed3RT_mean = mean(partner_mixed3RT_means);
    partner_mixed6RT_mean = mean(partner_mixed6RT_means);
    partner_mixed12RT_mean = mean(partner_mixed12RT_means);
    partner_mixedmonRT_mean = mean(partner_mixedmonRT_means);

    % write in tmp_data
    tmp_data = [subj_id you_high2RT_mean you_high3RT_mean you_high6RT_mean you_high12RT_mean you_highmonRT_mean you_mixed2RT_mean you_mixed3RT_mean you_mixed6RT_mean you_mixed12RT_mean you_mixedmonRT_mean partner_high2RT_mean partner_high3RT_mean partner_high6RT_mean partner_high12RT_mean partner_highmonRT_mean partner_mixed2RT_mean partner_mixed3RT_mean partner_mixed6RT_mean partner_mixed12RT_mean partner_mixedmonRT_mean];

    % write data to output file 'setsize_h1_output.tsv'
    fprintf(fid_run,'%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n',tmp_data);
end
fclose(fid_run);
