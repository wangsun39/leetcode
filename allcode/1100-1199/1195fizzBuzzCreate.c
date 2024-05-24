//    编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
//
//    如果这个数字可以被 3 整除，输出 "fizz"。
//    如果这个数字可以被 5 整除，输出 "buzz"。
//    如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
//    例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。
//
//    假设有这么一个类：
//
//    class FizzBuzz {
//      public FizzBuzz(int n) { ... }               // constructor
//      public void fizz(printFizz) { ... }          // only output "fizz"
//      public void buzz(printBuzz) { ... }          // only output "buzz"
//      public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
//      public void number(printNumber) { ... }      // only output the numbers
//    }
//    请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：
//
//    线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
//    线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
//    线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
//    线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。
//
//
//    提示：
//
//    本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。


typedef struct {
    int n;
    int cur;
    sem_t num3;
    sem_t num5;
    sem_t num15;
    sem_t other;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    obj->n = n;
    obj->cur = 1;
    sem_init(&obj->other, 0, 1);
    sem_init(&obj->num3, 0, 0);
    sem_init(&obj->num5, 0, 0);
    sem_init(&obj->num15, 0, 0);
    return obj;
}

void putNext(FizzBuzz* obj) {
    printf("post:%u\n",obj->cur);
    if (obj->cur % 15 == 0)
        sem_post(&obj->num15);
    else if (obj->cur % 3 == 0)
        sem_post(&obj->num3);
    else if (obj->cur % 5 == 0)
        sem_post(&obj->num5);
    else
        sem_post(&obj->other);
}

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    while (1) {
        int next = (obj->cur + 2) / 3 * 3;
        while (next % 15 == 0) {
            next += 3;
        }
        if (next > obj->n) break;
        sem_wait(&obj->num3);
        printFizz();
        obj->cur++;
        putNext(obj);
    }
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    while (1) {
        int next = (obj->cur + 4) / 5 * 5;
        while (next % 15 == 0) {
            next += 5;
        }
        if (next > obj->n) break;
        sem_wait(&obj->num5);
        printBuzz();
        obj->cur++;
        putNext(obj);
    }
}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while (1) {
        int next = (obj->cur + 14) / 15 * 15;
        if (next > obj->n) break;
        sem_wait(&obj->num15);
        printFizzBuzz();
        obj->cur++;
        putNext(obj);
    }
}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    while (1) {
        int next = obj->cur;
        while (next % 3 == 0 || next % 5 == 0) {
            next += 1;
        }
        if (next > obj->n) break;
        sem_wait(&obj->other);
        printNumber(obj->cur);
        obj->cur++;
        putNext(obj);
    }

}

void fizzBuzzFree(FizzBuzz* obj) {
    free(obj);
}


