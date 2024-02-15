file_path = 'ds_convergence/test_0.txt';

% Load Data from Text File
data = load(file_path);

% Finding key statistics for each population
% max_population = max(data(:));
% print(max_population);

% intial = data(1,:);
plot(data(1002,:));

% Add labels and title for better understanding
xlabel('ds');
ylabel('N(0,s)');
title('Final Solution g(s)=exp(-s) and mu(s)=s');
% title('Final Solution g(s)=exp(-s) and mu(s)=0');
% title('Final Solution g(s)=1 and mu(s)=0');

% % Create a Figure and Axes
% figure;
% axes_handle = axes;
% 
% % Set up Video Writer
% video_file_path = 'output_video_test_4.mov';
% video_writer = VideoWriter(video_file_path, 'MPEG-4');
% open(video_writer);
% 
% % Time Steps
% num_time_steps = size(data, 1);
% 
% % Determine y-axis limits based on the entire dataset
% y_min = min(data(:));
% y_max = max(data(:));
% 
% % Loop over Time Steps and Create Frames for the Video
% for t = 1:num_time_steps
%     % Plot the Solution at the Current Time Step
%     plot(axes_handle, 1:size(data, 2), data(t, :));
% 
%     % Find the Index of the Maximum Value in the Current Time Step
%     [~, max_index] = max(data(t, :));
% 
%     % Add Vertical Line at the Position of the Maximum Value
%     hold on;
%     plot([max_index, max_index], ylim, 'k--');  % Adjust line style and color as needed
%     hold off;
% 
%     % Customize Plot (e.g., labels, title, etc.)
%     xlabel('Size');
%     ylabel('Solution');
%     title(['Time Step: ' num2str(t)]);
% 
%     % Set y-axis limits
%     ylim([y_min, y_max]);
% 
%     % Add Pause (optional, adjust as needed)
%     pause(0.005);  % Adjust the duration of the pause
% 
%     % Capture Frame for the Video
%     frame = getframe(gcf);
%     writeVideo(video_writer, frame);
% 
%     % Clear Plot for the Next Time Step
%     cla(axes_handle);
% end
% 
% % Close Video Writer
% close(video_writer);
% 
% % Display Message
% disp(['Video saved to: ' video_file_path]);
% 


