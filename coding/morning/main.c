#include <ncurses.h>
#include <string.h>

#define MAX_TASKS 100
#define MAX_LEN 256

char tasks[MAX_TASKS][MAX_LEN];
int completed[MAX_TASKS];
int task_count = 0;
int current = 0;

void draw_tasks() {
    clear();
    mvprintw(0, 2, "TODO List - Arrow keys to navigate, [Space] to toggle, [a]dd, [d]elete, [q]uit");

    for (int i = 0; i < task_count; i++) {
        if (i == current) {
            attron(A_REVERSE); // highlight current selection
        }

        if (completed[i])
            mvprintw(i + 2, 4, "[x] %s", tasks[i]);
        else
            mvprintw(i + 2, 4, "[ ] %s", tasks[i]);

        if (i == current) {
            attroff(A_REVERSE);
        }
    }

    refresh();
}

void add_task(const char* new_task) {
    if (task_count >= MAX_TASKS) return;
    strncpy(tasks[task_count], new_task, MAX_LEN);
    completed[task_count] = 0;
    task_count++;
}

void input_task() {
    echo();
    curs_set(1);

    char buf[MAX_LEN];
    mvprintw(task_count + 3, 4, "Enter new task: ");
    getnstr(buf, MAX_LEN - 1);
    add_task(buf);

    noecho();
    curs_set(0);
}

void delete_current_task() {
    if (task_count == 0) return;
    for (int i = current; i < task_count - 1; i++) {
        strcpy(tasks[i], tasks[i + 1]);
        completed[i] = completed[i + 1];
    }
    task_count--;
    if (current >= task_count && task_count > 0) current--;
}

int main() {
    initscr();
    noecho();
    curs_set(0);
    keypad(stdscr, TRUE);

    add_task("Task 1");
    add_task("Task 2");
    add_task("Task 3");

    int ch;
    while (1) {
        draw_tasks();
        ch = getch();

        if (ch == 'q') break;
        else if (ch == KEY_UP && current > 0) current--;
        else if (ch == KEY_DOWN && current < task_count - 1) current++;
        else if (ch == ' ') completed[current] = !completed[current];
        else if (ch == 'a') input_task();
        else if (ch == 'd') delete_current_task();
    }

    endwin();
    return 0;
}