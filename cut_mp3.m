% 其实可以参考遍历文件夹的方法(深度遍历广度遍历)
flag = 1;
path = '/Users/lixinhao/Desktop/DAM_HW1/3160105158/';

for flag = flag:100
    F = floor((flag-1)/10);
    switch(F)
        case 0
            filename = [path, 'Male Singer/A许嵩/', num2str(flag), '.mp3'];
        case 1
            filename = [path, 'Male Singer/B陈奕迅/', num2str(flag), '.mp3'];
        case 2
            filename = [path, 'Male Singer/C林俊杰/', num2str(flag), '.mp3'];
        case 3
            filename = [path, 'Male Singer/D华晨宇/', num2str(flag), '.mp3'];
        case 4
            filename = [path, 'Male Singer/E陈鸿宇/', num2str(flag), '.mp3'];
        case 5
            filename = [path, 'Female Singer/F王菲/', num2str(flag), '.mp3'];
        case 6
            filename = [path, 'Female Singer/G陈粒/', num2str(flag), '.mp3'];
        case 7
            filename = [path, 'Female Singer/H杨丞琳/', num2str(flag), '.mp3'];
        case 8
            filename = [path, 'Female Singer/I郭静/', num2str(flag), '.mp3'];
        case 9
            filename = [path, 'Female Singer/J张碧晨/', num2str(flag), '.mp3'];
    end
    [x, fs] = audioread(filename);
    start_time = 60;
    end_time = 120;
    new = x((fs*start_time+1) : fs*end_time, 1);
    audiowrite([num2str(flag), '.mp4'], new, fs); 
end
