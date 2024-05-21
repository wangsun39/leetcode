//    给你一个类：
//
//    class FooBar {
//      public void foo() {
//        for (int i = 0; i < n; i++) {
//          print("foo");
//        }
//      }
//
//      public void bar() {
//        for (int i = 0; i < n; i++) {
//          print("bar");
//        }
//      }
//    }
//    两个不同的线程将会共用一个 FooBar 实例：
//
//    线程 A 将会调用 foo() 方法，而
//    线程 B 将会调用 bar() 方法
//    请设计修改程序，以确保 "foobar" 被输出 n 次。
//
//
//
//    示例 1：
//
//    输入：n = 1
//    输出："foobar"
//    解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
//    示例 2：
//
//    输入：n = 2
//    输出："foobarfoobar"
//    解释："foobar" 将被输出两次。
//
//
//    提示：
//
//    1 <= n <= 1000


typedef struct {
    int n;
    sem_t foo;
    sem_t bar;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    sem_init(&obj->foo, 0, 1);
    sem_init(&obj->bar, 0, 0);
    return obj;
}

void foo(FooBar* obj) {

    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->foo);
        // printFoo() outputs "foo". Do not change or remove this line.
        printFoo();
        sem_post(&obj->bar);
    }
}

void bar(FooBar* obj) {

    for (int i = 0; i < obj->n; i++) {
        sem_wait(&obj->bar);
        // printBar() outputs "bar". Do not change or remove this line.
        printBar();
        sem_post(&obj->foo);
    }
}

void fooBarFree(FooBar* obj) {
    free(obj);
}


