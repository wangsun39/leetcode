//    现有函数 printNumber 可以用一个整数参数调用，并输出该整数到控制台。
//
//    例如，调用 printNumber(7) 将会输出 7 到控制台。
//    给你类 ZeroEvenOdd 的一个实例，该类中有三个函数：zero、even 和 odd 。ZeroEvenOdd 的相同实例将会传递给三个不同线程：
//
//    线程 A：调用 zero() ，只输出 0
//    线程 B：调用 even() ，只输出偶数
//    线程 C：调用 odd() ，只输出奇数
//    修改给出的类，以输出序列 "010203040506..." ，其中序列的长度必须为 2n 。
//
//    实现 ZeroEvenOdd 类：
//
//    ZeroEvenOdd(int n) 用数字 n 初始化对象，表示需要输出的数。
//    void zero(printNumber) 调用 printNumber 以输出一个 0 。
//    void even(printNumber) 调用printNumber 以输出偶数。
//    void odd(printNumber) 调用 printNumber 以输出奇数。
//
//
//    示例 1：
//
//    输入：n = 2
//    输出："0102"
//    解释：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
//    示例 2：
//
//    输入：n = 5
//    输出："0102030405"
//
//
//    提示：
//
//    1 <= n <= 1000


typedef struct {
    int n;
    sem_t zero;
    sem_t even;
    sem_t odd;
} ZeroEvenOdd;

ZeroEvenOdd* zeroEvenOddCreate(int n) {
    ZeroEvenOdd* obj = (ZeroEvenOdd*) malloc(sizeof(ZeroEvenOdd));
    obj->n = n;
    sem_init(&obj->zero, 0, 1);
    sem_init(&obj->even, 0, 0);
    sem_init(&obj->odd, 0, 0);
    return obj;
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.

void zero(ZeroEvenOdd* obj) {

    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->zero);
        // printFoo() outputs "foo". Do not change or remove this line.
        printNumber(0);
        if (i & 1)
            sem_post(&obj->even);
        else
            sem_post(&obj->odd);
    }
}

void even(ZeroEvenOdd* obj) {

    for (int i = 1; i < obj->n; i+=2) {
        sem_wait(&obj->even);
        // printFoo() outputs "foo". Do not change or remove this line.
        printNumber(i + 1);
        sem_post(&obj->zero);
    }
}

void odd(ZeroEvenOdd* obj) {

    for (int i = 0; i < obj->n; i+=2) {
        sem_wait(&obj->odd);
        // printFoo() outputs "foo". Do not change or remove this line.
        printNumber(i + 1);
        sem_post(&obj->zero);
    }
}

void zeroEvenOddFree(ZeroEvenOdd* obj) {
    free(obj);
}


