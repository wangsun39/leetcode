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
    pthread_mutex_t lock;
    pthread_cond_t  cond;
} FizzBuzz;

FizzBuzz* fizzBuzzCreate(int n) {
    FizzBuzz* obj = (FizzBuzz*) malloc(sizeof(FizzBuzz));
    memset(obj, 0, sizeof(FizzBuzz));
    obj->n = n;
    obj->cur = 1;
    return obj;
}

// printFizz() outputs "fizz".
void fizz(FizzBuzz* obj) {
    pthread_mutex_lock(&obj->lock);
    int next = obj->cur;
    while (next % 3 || next % 15 == 0) {
        next++;
        if (next > obj->n){
            pthread_mutex_unlock(&obj->lock);
            return;
        }
    }

    while (obj->cur % 3 != 0 || 0 == obj->cur % 5) {
        pthread_cond_wait(&obj->cond, &obj->lock);
    }
    printFizz();
    obj->cur++;

    pthread_cond_signal(&obj->cond);
    pthread_mutex_unlock(&obj->lock);
}

// printBuzz() outputs "buzz".
void buzz(FizzBuzz* obj) {
    pthread_mutex_lock(&obj->lock);
    int next = obj->cur;
    while (next % 5 || next % 15 == 0) {
        next++;
        if (next > obj->n){
            pthread_mutex_unlock(&obj->lock);
            return;
        }
        next++;
    }
    while (obj->cur % 5 != 0 || 0 == obj->cur % 3) {
        pthread_cond_wait(&obj->cond, &obj->lock);
    }
    printBuzz();
    obj->cur++;

    pthread_cond_signal(&obj->cond);
    pthread_mutex_unlock(&obj->lock);

}

// printFizzBuzz() outputs "fizzbuzz".
void fizzbuzz(FizzBuzz* obj) {
    while(true) {
        pthread_mutex_lock(&obj->lock);
        int next = obj->cur;
        while (next % 15) {
            next++;
            if (next > obj->n) {
                pthread_mutex_unlock(&obj->lock);
                return;
            }
        }
        while (obj->cur % 15 != 0) {
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
        printFizzBuzz();
        obj->cur++;

        pthread_cond_signal(&obj->cond);
        pthread_mutex_unlock(&obj->lock);
    }

}

// You may call global function `void printNumber(int x)`
// to output "x", where x is an integer.
void number(FizzBuzz* obj) {
    while(true) {
        pthread_mutex_lock(&obj->lock);
        int next = obj->cur;
        if (next > obj->n) {
                pthread_mutex_unlock(&obj->lock);
                return;
            }
        while (next % 5 == 0 || 0 == next % 3) {
            next++;
            if (next > obj->n) {
                pthread_mutex_unlock(&obj->lock);
                return;
            }
        }
        while (obj->cur % 5 == 0 || 0 == obj->cur % 3) {
            pthread_cond_wait(&obj->cond, &obj->lock);
        }
        printNumber(obj->cur);
        obj->cur++;

        pthread_cond_signal(&obj->cond);
        pthread_mutex_unlock(&obj->lock);
    }

}

void fizzBuzzFree(FizzBuzz* obj) {
    free(obj);
}


