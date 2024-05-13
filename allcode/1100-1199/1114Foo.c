//给你一个类：
//
//public class Foo {
//  public void first() { print("first"); }
//  public void second() { print("second"); }
//  public void third() { print("third"); }
//}
//三个不同的线程 A、B、C 将会共用一个 Foo 实例。
//
//线程 A 将会调用 first() 方法
//线程 B 将会调用 second() 方法
//线程 C 将会调用 third() 方法
//请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。
//
//提示：
//
//尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
//你看到的输入格式主要是为了确保测试的全面性。
//
//
//示例 1：
//
//输入：nums = [1,2,3]
//输出："firstsecondthird"
//解释：
//有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。正确的输出是 "firstsecondthird"。
//示例 2：
//
//输入：nums = [1,3,2]
//输出："firstsecondthird"
//解释：
//输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正确的输出是 "firstsecondthird"。
//
//
//提示：
//nums 是 [1, 2, 3] 的一组排列


typedef struct {
    // User defined data may be declared here.
    pthread_mutex_t myMutex;
    int flag;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));

    // Initialize user defined data here.
    memset(obj, 0, sizeof(Foo));
    return obj;
}

void first(Foo* obj) {

    // printFirst() outputs "first". Do not change or remove this line.
    while(true)
    {
        pthread_mutex_lock(&obj->myMutex);
        printFirst();
        obj->flag++;
        pthread_mutex_unlock(&obj->myMutex);
        break;
    }

}

void second(Foo* obj) {

    // printSecond() outputs "second". Do not change or remove this line.

    while(true)
    {
        pthread_mutex_lock(&obj->myMutex);
        if (obj->flag < 1)
        {
            pthread_mutex_unlock(&obj->myMutex);
            continue;
        }
        printSecond();
        obj->flag++;
        pthread_mutex_unlock(&obj->myMutex);
        break;
    }
}

void third(Foo* obj) {

    // printThird() outputs "third". Do not change or remove this line.

    while(true)
    {
        pthread_mutex_lock(&obj->myMutex);
        if (obj->flag < 2)
        {
            pthread_mutex_unlock(&obj->myMutex);
            continue;
        }
        printThird();
        obj->flag++;
        pthread_mutex_unlock(&obj->myMutex);
        break;
    }
}

void fooFree(Foo* obj) {
    // User defined data may be cleaned up here.

}


