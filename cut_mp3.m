% ��ʵ���Բο������ļ��еķ���(��ȱ�����ȱ���)
flag = 1;
path = '/Users/lixinhao/Desktop/DAM_HW1/3160105158/';

for flag = flag:100
    F = floor((flag-1)/10);
    switch(F)
        case 0
            filename = [path, 'Male Singer/A����/', num2str(flag), '.mp3'];
        case 1
            filename = [path, 'Male Singer/B����Ѹ/', num2str(flag), '.mp3'];
        case 2
            filename = [path, 'Male Singer/C�ֿ���/', num2str(flag), '.mp3'];
        case 3
            filename = [path, 'Male Singer/D������/', num2str(flag), '.mp3'];
        case 4
            filename = [path, 'Male Singer/E�º���/', num2str(flag), '.mp3'];
        case 5
            filename = [path, 'Female Singer/F����/', num2str(flag), '.mp3'];
        case 6
            filename = [path, 'Female Singer/G����/', num2str(flag), '.mp3'];
        case 7
            filename = [path, 'Female Singer/H��ة��/', num2str(flag), '.mp3'];
        case 8
            filename = [path, 'Female Singer/I����/', num2str(flag), '.mp3'];
        case 9
            filename = [path, 'Female Singer/J�ű̳�/', num2str(flag), '.mp3'];
    end
    [x, fs] = audioread(filename);
    start_time = 60;
    end_time = 120;
    new = x((fs*start_time+1) : fs*end_time, 1);
    audiowrite([num2str(flag), '.mp4'], new, fs); 
end
